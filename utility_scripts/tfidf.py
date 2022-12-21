import librarian
import os

CATALOG_PATH = 'texts'

with open('resources/badwords.txt') as f:
	BADWORDS = set([line.strip() for line in f.readlines()]) | set([line.strip() + 's' for line in f.readlines()])

def get_keywords_from_file_and_directory(filepath, dirpath):
	with open(filepath) as f:
		filetext = f.read()
	tf_dict = librarian.term_dict(filetext)
	tf_dicts = librarian.term_frequency_dicts_from_directory(dirpath)
	df_dict = librarian.document_frequency_dict_from_tf_dicts(tf_dicts)
	keywords = librarian.keywords(tf_dict, df_dict, tf_dicts)
	stopwords = librarian.stopwords()
	keywords = [kword for kword, score in keywords if not kword in stopwords]
	return keywords

def get_dicts(dirpath):
	tf_dicts = librarian.term_frequency_dicts_from_directory(dirpath)
	df_dict = librarian.document_frequency_dict_from_tf_dicts(tf_dicts)
	return tf_dicts, df_dict

def get_keywords_from_file_and_dicts(filepath, df_dict, tf_dicts):
	with open(filepath) as f:
		filetext = f.read()
	tf_dict = librarian.term_dict(filetext)
	keywords = librarian.keywords(tf_dict, df_dict, tf_dicts)
	stopwords = librarian.stopwords()
	keywords = [kword for kword, score in keywords if not kword in stopwords]
	return keywords

def get_keywords_from_files_and_directory(filepaths, dirpath):
	tf_dicts = librarian.term_frequency_dicts_from_directory(dirpath)
	df_dict = librarian.document_frequency_dict_from_tf_dicts(tf_dicts)
	for filepath in filepaths:
		with open(filepath) as f:
			filetext = f.read()
		tf_dict = librarian.term_dict(filetext)
		
		keywords = librarian.keywords(tf_dict, df_dict, tf_dicts)
		stopwords = librarian.stopwords()
		keywords = [kword for kword, score in keywords if not kword in stopwords]
		yield (filepath, keywords)

if __name__ == "__main__":

	filepaths = [os.path.join('texts',fname) for fname in os.listdir('texts')]
	print(get_keywords_from_file_and_directory('texts/jimi-hendrix.txt', 'texts'))
	# path_keyword_list_pairs = list(get_keywords_from_files_and_directory(filepaths, 'texts'))
	# for path, keyword_list in path_keyword_list_pairs:
	#     keyword_list = [kw for kw in keyword_list if librarian.is_clean(kw, BADWORDS)]
	#     print(path)
	#     print(', '.join(keyword_list[:50]))