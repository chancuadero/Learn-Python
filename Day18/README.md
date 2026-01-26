This is Day 18 of learning Python

Topic: Alternation and non-capturing groups
Summary: Alternation and non-capturing groups are key regular expression features that allow for more complex pattern matching and extraction. Alternation acts as an "OR" operator, while non-capturing groups are used to group patterns without saving the matched content.
Example:
import re
text = "invoice*882.pdf, receipt_441.docx, photo_99.png"
regex = r"(?:invoice|receipt)*\d+\.(?:pdf|docx)"
matches = re.findall(regex,text)
print(matches)
#output: ['invoice_882.pdf', 'receipt_441.docx']
