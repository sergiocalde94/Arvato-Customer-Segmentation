from pathlib import Path


# PATH_PROJECT will be called from the root of the project or from one of the subfolders
PATH_PROJECT = Path('.') if Path('.').resolve().name == 'Arvato-Customer-Segmentation' else Path('..')
PATH_DATA = PATH_PROJECT / 'data'
PATH_FILE_ATTRIBUTES = PATH_DATA / 'feature_attributes.xlsx'
PATH_SUBMISSIONS = PATH_PROJECT / 'submissions'
SEP = ';'
NA_VALUES = [0, -1, 'X', 'XX']
