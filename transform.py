def get_transform(output, context):
    if "<result>" not in output:
        return output
    try:
        return {
            "predication": output.split("<result>")[1].split("</result>")[0].strip(),
            "thinking": output.split("<thinking>")[1].split("</thinking>")[0].strip(),
        }
    except Exception as e:
        raise ValueError(f"Error parsing output: {e}")
