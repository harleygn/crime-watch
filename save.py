from datetime import datetime


def save_report(report, save_dir, name):
    """
    Function to save a dataframe as a CSV file with a name based on current date
    and time plus a name label
    :param report: Dataframe containing data to save
    :param save_dir: String containing filepath of directory in which to save
    :param name: String containing optional filename
    :return: None
    """
    # Builds a filename based on current date and time plus a name label
    filename = str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + '_' + name \
               + '.csv'
    # Joins the filename to the directory path to get a full filepath
    filepath = save_dir + filename
    # Uses the dataframe's built in method to save as a CSV
    report.to_csv(filepath)
