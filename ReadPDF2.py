import fitz

doc = fitz.open("Mortgage_Illustration.pdf") # open a document

text_as_str = ''

for page in doc: # iterate the document pages
    text = page.get_text() # .encode("utf8") get plain text (I've commented out the encode to UTF-8)
    text_as_str += str(text)

# Find loan amount
def loan_amount():
    start_tag = 'loan to be granted: '
    end_tag = '.'
    start_index = text_as_str.find(start_tag) + len(start_tag)
    end_index = text_as_str.find(end_tag,start_index)
    loan_amount = text_as_str[start_index:end_index]
    return(loan_amount)
