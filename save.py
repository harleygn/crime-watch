from datetime import datetime


def save_report(report, save_dir, name):
    filename = str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + '_' + name \
               + '.csv'
    filepath = save_dir + filename
    report.to_csv(filepath)
