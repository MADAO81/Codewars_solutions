# https://www.codewars.com/kata/597770e98b4b340e5b000071/train/python


# class FileNameExtractor:
#     @staticmethod
#     def extract_file_name(dirty_file_name):
#         split_fn = dirty_file_name.split(".")
#         extension = split_fn[1]
#         file_name = "_".join(split_fn[0].split("_")[1:])
#         return f"{file_name}.{extension}"


class FileNameExtractor:
    @staticmethod
    def extract_file_name(fname):
        return fname.split('_', 1)[1].rsplit('.', 1)[0]
