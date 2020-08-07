from helpers.regex import match, replace

def _get_xml_tag(key, value):
    if isinstance(value, list):
        return "".join(to_xml({key: i}) for i in value)

    closing_tag = match(r"[\w:]+", key)
    return f"<{key}>{to_xml(value)}</{closing_tag}>"


def to_xml(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bool):
        return str(data).lower()
    elif isinstance(data, int) or isinstance(data, float):
        return str(data)

    return "".join(_get_xml_tag(k, v) for (k, v) in data.items())


def _remove(regex, xml):
    return xml[len(match(regex, xml)) :]


def to_dict(xml):
    def _parse_xml():
        nonlocal xml

        if xml[0] != "<" or xml[:2] == "</":
            result = match(r"[^<]*", xml)
            xml = xml[len(result) :]
            if result == "true":
                return True
            if result == "false":
                return False
            if match(r"^\d+$", result):
                return int(result)
            if match(r"^\d+\.\d+$", result):
                return float(result)

            return result

        result = {}

        while xml[:2] and xml[:2] != "</":
            tag_name = match(r"\<([\w:]+?)(\s|\>)", xml, 1)

            if match(r"^\<[^\>]+\/\>", xml):
                result[tag_name] = ""
                xml = _remove(r".+?\>", xml)
                continue

            xml = _remove(r".+?\>", xml)

            # Multiple sibling tags with the same name -> list
            if tag_name in result and not isinstance(result[tag_name], list):
                result[tag_name] = [result[tag_name]]

            if tag_name in result and isinstance(result[tag_name], list):
                result[tag_name].append(_parse_xml())
            else:
                result[tag_name] = _parse_xml()

            xml = _remove(r"\<.+?\>", xml)

        return result

    declaration = match(r"^\<\?xml.*\?\>", xml)
    if declaration:
        xml = xml[len(declaration) :]

    return _parse_xml()
