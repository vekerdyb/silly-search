from Index import SimpleIndex

ind = SimpleIndex('data.csv')
ind.delete()
ind.add_documents_from_directory('htmls/*.html')