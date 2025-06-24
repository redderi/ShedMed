from datetime import date, datetime


def parse_date(value):
    if isinstance(value, (date, datetime)):
        return value.strftime('%Y-%m-%d')
    if not isinstance(value, str):
        raise ValueError(f"Неверный тип даты: {type(value)}")
        
    formats = ['%d.%m.%Y', '%d-%m-%Y', '%Y-%m-%d']
    for fmt in formats:
        try:
            parsed_date = datetime.strptime(value.strip(), fmt)
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            continue
    raise ValueError(f"Неверный формат даты: {value}")