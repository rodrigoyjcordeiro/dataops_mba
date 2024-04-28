import datetime


def generate_data_file_name_bronze():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y%m%d%H%M%S")
    file_name = f"dados_brutos_universidades_{formatted_time}"
    return file_name


def generate_data_file_name_silver():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y%m%d%H%M%S")
    file_name = f"ingestao_universidades_{formatted_time}"
    return file_name


def generate_metadata_file_name():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y%m%d%H%M%S")
    file_name = f"metadado_universidades_{formatted_time}"
    return file_name
