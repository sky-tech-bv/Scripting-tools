def main():
    # It is the code dictionary to create code text
    code = {'А':'Б', 'а':'б', 'Б':'В', 'б':'в', 'В':'Г', 'в':'г', 'Г':'Д', 'г':'д', 'Д':'Е', 'д':'е', 
            'Е':'Ж', 'е':'ж', 'Ж':'З', 'ж':'з', 'З':'И', 'з':'и', 'И':'Й', 'и':'й', 'Й':'К', 'й':'к', 
            'К':'Л', 'к':'л', 'Л':'М', 'л':'м', 'М':'Н', 'м':'н', 'Н':'О', 'н':'о', 'О':'П', 'о':'п', 
            'П':'Р', 'п':'р', 'Р':'С', 'р':'с', 'С':'Т', 'с':'т', 'Т':'У', 'т':'у', 'У':'Ф', 'у':'ф', 
            'Ф':'Х', 'ф':'х', 'Х':'Ц', 'х':'ц', 'Ц':'Ч', 'ц':'ч', 'Ч':'Ш', 'ч':'ш', 'Ш':'Щ', 'ш':'щ', 
            'Щ':'Ь', 'щ':'ь', 'Ь':'Ъ', 'ь':'ъ', 'Ъ':'Ы', 'ъ':'Ы', 'Ы':'Э', 'ы':'э', 'Э':'Ю', 'э':'ю', 
            'Ю':'Я', 'ю':'я', 'Я':'А', 'я':'а', '.':',', ',':'.'}
    
    # Open and read file with code text
    infile = open('secter_code.txt', 'r')
    code_text = infile.read()
    infile.close()
    
    # Change simbols help to dictionary 'code'
    result = ''
    for ch in code_text:
        for key, value in code.items():
            if value == ch:
                ch = key
        result += ch
            
    # Open outfile to write the original text to it
    outfile = open('out_text.txt', 'w')
    outfile.write(result)
    outfile.close()

    print('Готово!')
if __name__ == '__main__':
    main()