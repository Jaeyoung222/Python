def P6(input_filename: str, out_filename: str) -> None :
    ##### Write your Code Here #####
    with open(input_filename,'r') as input_file, open(out_filename, 'w') as output_file :
        for line in input_file :
            #write each line of input_filename that replace space to comma into out_filename
            output_file.write(line.replace(' ',','))
    ##### End of your code #####