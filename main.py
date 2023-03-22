from datetime import datetime, date
from llms import make_model
# from callbacks import GantryCallback
from prompts import GOOD_PROMPT

# default_model = make_model(GOOD_PROMPT, callbacks=[GantryCallback("dtparse", env="dev")])

def DTParse(model):
    def dtparse(req):
        return model(date=str(date.today()), time=datetime.now().strftime("%H:%M:%S"), request=req)
    return dtparse

# dtparse = DTParse(default_model)

def main():
    # for req in ["tomorrow at 3pm", "next saturday", "the day after tomorrow", "monday morning", "the second sunday of next month"]:
    #     print(f"{req} -> {dtparse(req)}")

    req = 'one week from yesterday'
    print(f'{req} -> {dtparse(req)}')

if __name__ == '__main__':
    main()
