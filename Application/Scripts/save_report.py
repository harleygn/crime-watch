from datetime import datetime


def save(data, save_dir, postcode, radius, name='report'):
    postcode = postcode.replace(' ', '_')
    location = postcode + '_' + str(radius)
    # Builds a filename based on current date and time plus a name label
    filename = str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + '_' + location + '_' + name + '.csv'
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
