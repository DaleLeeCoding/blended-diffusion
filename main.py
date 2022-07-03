from optimization.image_editor import ImageEditor
from optimization.arguments import get_arguments
import pandas as pd


if __name__ == "__main__":
    args = get_arguments()
    xlsx = pd.read_excel('./DrawBench Prompts.xlsx')
    for pr, cat in zip(xlsx['Prompts'], xlsx['Category']):
        args.prompt = pr
        args.category = cat
        image_editor = ImageEditor(args)
        image_editor.edit_image_by_prompt()
    # image_editor.reconstruct_image()
