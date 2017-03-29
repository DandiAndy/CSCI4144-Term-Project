if __name__ == '__main__':
    data_file_name = "pokedata2"
    strip_file_name = "raw/page"
    strip_file_count = 10
    key = "<p><strong>"
    end = "</"
    team_check = 0
    
    # count the amount of teams and mons found to print at the end.
    team_count = 0
    poke_count = 0
    
    #open data file and write teams as lines
    df = open(data_file_name, "w+")
    df.seek(0)
    df.write("Member#1\tMember#2\tMember#3\tMember#4\tMember#5\tMember#6\t\n".expandtabs(20))
    print("...stripping webpage of data...")
    for i in range(1, strip_file_count+1):
        sf = open('{}{}'.format(strip_file_name, i), "r+")
        for line in sf:
            if key in line:
                if line.split(key)[1][0] != '<':
                    team_check += 1
                    poke_count += 1
                    df.write("{}\t".format((line.split(key))[1].split(end)[0]).expandtabs(20))
                    if team_check == 6:
                        team_count += 1
                        team_check = 0
                        df.write("\n")
        sf.close()
    print("Teams Found: {}, Total Mons Found: {}".format(team_count, poke_count))
    df.close()
    
                
