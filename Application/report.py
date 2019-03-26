def get_total_crimes(input_data):
    """
    Gets the total number of crimes recorded
    :param input_data: Data sent from read_crimes
    :return: Int: Number of crimes
    """
    number_of_crimes = len(input_data)
    return number_of_crimes


def get_data_types(input_data, data_position):
    """
    Gets a list of all crimes or outcomes
    :param input_data: Data sent from read_crimes
    :param data_position: The location in each crime record of the data to be recorded
    :return: List: Every crime or outcome in input_data
    """
    total_data_types_list = []
    for i in range(0,len(input_data)):
        if input_data[i][data_position] != "":  # If the data in the data_position is not blank
            total_data_types_list.append(input_data[i][data_position])
    return total_data_types_list


def get_unique_data_types(data_list):
    """
    Gets all unique values in data_list
    :param data_list: List of all crimes or outcomes
    :return: List: unique list of crimes or outcomes
    """
    data_set = set(data_list)  # Turning the data to a set removes all duplicates
    unique_data_types = list(data_set)  # Transfer set back to list so it can be manipulated
    return unique_data_types


def convert_data_to_file_format(data, data_title):
    """
    Coverts crime_and_numbers or outcomes_and_numbers to file friendly formats
    :param data: Data being passed in to be converted
    :param data_title: Title of data to be shown in report
    :return: List: Contains all same data with a title and in different format
    """
    new_format = [[data_title, ""]]  # save_report function requires lists of lists

    for i in range(0, len(data)):
        new_format.append(data[i])  # Append the list i from data to new_format

    new_format.append("\n")  # Appended to create a gap between data in report
    return new_format


def get_number_of_data_types(total_data_types, data_types):
    """
    Gets a list of lists containing all crimes or outcomes and how often they occur
    :param total_data_types: List of all crimes or outcomes
    :param data_types: List of all unique crimes or outcomes
    :return: 2D Array: Various lists of crime or outcome in data_types and how often they occur in total_data_types
    """
    data_types_and_number = []

    for i in range(0, len(data_types)):  # For each type of data
        temp_count = 0

        for j in range(0, len(total_data_types)):  # For every value recorded in total_data_types
            if total_data_types[j] == data_types[i]:
                temp_count += 1

        temp_list = [data_types[i], str(temp_count)]  # Append the crime or outcome type and the frequency
        data_types_and_number.append(temp_list)

    data_types_and_number.sort(key=lambda x: x[1], reverse=True)  # Sort values by the frequency

    for i in range(0, len(data_types_and_number)):  # Convert frequency's to strings for report
        data_types_and_number[i][1] = str(data_types_and_number[i][1])

    return data_types_and_number


def get_most_popular_month(input_data):
    """
    Get the month where most crimes were committed
    :param input_data: Data sent from read_crimes
    :return: Str: The month with the most crime
    """
    months = get_data_types(input_data, 1)  # Get a list of all months recorded
    return max(set(months), key=months.count)  # Get the most common month from the months list


def create_report_data(input_data):
    """
    Calls all functions to collate data for report then puts report in correct format to be passed to save_report
    :param input_data: Data sent from read_crimes
    :return: List: The report to be passed to save_report
    """
    total_crimes = get_total_crimes(input_data)
    total_crimes_types_list = get_data_types(input_data, 9)
    total_outcome_types_list = get_data_types(input_data, 10)
    unique_crime_types_list = get_unique_data_types(total_crimes_types_list)
    unique_outcome_types_list = get_unique_data_types(total_outcome_types_list)
    crimes_and_numbers = get_number_of_data_types(total_crimes_types_list, unique_crime_types_list)
    outcomes_and_numbers = get_number_of_data_types(total_outcome_types_list, unique_outcome_types_list)
    most_popular_month = get_most_popular_month(input_data)
    crimes_for_file = convert_data_to_file_format(crimes_and_numbers, "Crimes")
    outcomes_for_file = convert_data_to_file_format(outcomes_and_numbers, "Outcomes")

    report = [["Total Crimes", str(total_crimes), "\n"], ["Most Popular Month for Crimes", most_popular_month, "\n"]]

    for i in range(0, len(crimes_for_file)):
        report.append(crimes_for_file[i])

    for i in range(0, len(outcomes_for_file)):
        report.append(outcomes_for_file[i])

    return report
