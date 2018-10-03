import os


def i_feel_pretty():
    cw = os.getcwd()
    f = open(r"All_data.txt", "a+")
    newdir = cw + "/Data/tweet"
    os.chdir(newdir)
    p = os.listdir(newdir)
    for nea in p:
        a = nea
        try:
            if (".txt" not in a):
                os.rename(a, a + '.txt')
                a = nea + ".txt"
            lio = open(nea, "r", encoding='utf-8', errors='ignore').read()
            lio.replace("{", " ")
            lio.replace("}", " ")
            li = lio.split(",")
            formatted_string = li[2] + " , " + li[7] + "\n\n\n"
            f.write(formatted_string)
        except IndexError:
            pass
        except FileNotFoundError:
            lio = open(nea + ".txt", "r", encoding='utf-8', errors='ignore').read()
            lio.replace("{", " ")
            lio.replace("}", " ")
            li = lio.split(",")
            formatted_string = li[2] + " , " + li[7] + "\n\n\n"
            f.write(formatted_string)
        except:
            pass

    f.close()


i_feel_pretty()
