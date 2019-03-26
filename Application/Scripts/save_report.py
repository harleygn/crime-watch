def save(data, save_dir, name='report'):
    # Builds a filename based on current date and time plus a name label
    filename = '/' + name + '.csv'
    # Joins the filename to the directory path to get a full filepath
    filepath = save_dir + filename
    joined_rows = []
    for row in data:
        joined = ','.join(row)
        joined_rows.append(joined)
    flattened_list = '\n'.join(joined_rows)
    with open(filepath, 'w') as save_file:
        save_file.write(flattened_list)
    print("Crime data file successfully saved in the root directory as: "+ filename)
