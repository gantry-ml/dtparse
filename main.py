from datetime import datetime, date
from llms import make_model
from callbacks import GantryCallback
from prompts import PROMPT

model = make_model(PROMPT, callbacks=[GantryCallback("dtparse", env="dev")])

dtparse = lambda req: model(date=str(date.today()), time=datetime.now().strftime("%H:%M:%S"), request=req)

def main():
    # for req in ["tomorrow at 3pm", "next saturday", "the day after tomorrow", "monday morning", "the second sunday of next month"]:
    #     print(f"{req} -> {dtparse(req)}")

    req = 'one week from yesterday'
    print(f'{req} -> {dtparse(req)}')

if __name__ == '__main__':
    main()
