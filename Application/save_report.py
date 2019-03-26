def save(data, save_dir, name='report'):
    """
    Saves an array of data as a CSV
    :param data: an array of data
    :param save_dir: the location in which the save the CSV
    :param name: an optional label to add to the file, defaults to 'report'
    :return: None
    """
    # Builds a filename
    filename = name + '.csv'
    # Joins the filename to the directory path to get a full filepath
    filepath = save_dir + filename
    joined_rows = []
    # Rejoins the objects in each row into a comma delimited string
    for row in data:
        joined = ','.join(row)
        joined_rows.append(joined)
    # Rejoins each row into a single string delimited by newline chars
    flattened_list = '\n'.join(joined_rows)
    with open(filepath, 'w') as save_file:
        save_file.write(flattened_list)
    print('Crime data file successfully saved in the root directory as: ' + filename)
