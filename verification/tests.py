init_code = """
if not "Lamp" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Lamp'?")

Lamp = USER_GLOBAL['Lamp']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. First lamp": [
        prepare_test(middle_code='''lamp_1 = Lamp()
lamp_1.light()''',
                     test="lamp_1.light()",
                     answer="Red")
    ],
    "2. Second lamp": [
        prepare_test(middle_code='''lamp_2 = Lamp()
lamp_2.light()
lamp_2.light()''',
                     test="lamp_2.light()",
                     answer="Blue")
    ],
    "3. Third lamp": [
        prepare_test(middle_code='''lamp_3 = Lamp()
lamp_3.light()
lamp_3.light()
lamp_3.light()''',
                     test="lamp_3.light()",
                     answer="Yellow")
    ],
    "4. Fourth lamp": [
        prepare_test(middle_code='''lamp_4 = Lamp()
lamp_4.light()
lamp_4.light()
lamp_4.light()
lamp_4.light()''',
                     test="lamp_4.light()",
                     answer="Green")
    ]

}
