def enfermedad():
    cadena = input('Ingrese la cadena ADN del paciente: ')

    #ADN personas sana
    sana = 'ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGAaGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGC'
    sana1 = 'atggaggacagccccactatggttagagtggacagccccactatggttaggggtgaaaaccaggtttcgccatgtcaagggagaaggtgcttccccaaagctcttggctatgtcaccggtgacatgaaaaaacttgccaaccagcttaaagacaaacccgtggtgctccagttcattgactggattctccggggcatatcccaagtggtgttcgtcaacgaccccgtcagtggaatcctgattctggtaggacttcttgttcagaacccctggtgggctctcactggctggctgggaacagtggtctccactctgatggc'
    sana2 = 'ttatatacta actacataat gacctgttca aaccagactc tatttaatga actgtgaatttacacagagg ccattttaaa tgggtcaccc catttaggat tagtggatct caaattattaaccaaacatc actccatttc aaagtaaaat attacgccac cagcgatttg atttattggctcttccattg ccactgagca atgcccagga agcaggcaca ttgccaagga ctgggggcatcttgactagg aagctcctcg tttgtgtgag cgtgggtcag accgccaaag taggacttcatcgtttacct acctattatc aatatggtgc ttgaatatat tcctataact gtagaacagtgtggaaagtg atggtaactt tgaagttgtt catgttttat tggctttgtt ttaattgaca'
    sana3 = 'gtcagagtcg gctcagcctg cgccggggaa catcggccgc ctccagctcc cggcgcggcccggcccggcc cggctcggcc gcctcagcag acgccgcctg ccctgcagcc atgaggcccccgcagtgtct gctgcacacg ccttccctgg cttccccact ccttctcctc ctcctctggctcctgggtgg aggagtgggg gctgagggcc gggaggatgc agagctgctg gtgacggtgcgtgggggccg gctgcggggc attcgcctga agacccccgg gggccctgtc tctgctttcctgggcatccc ctttgcggag ccacccatgg gaccccgtcg ctttctgcca ccggagcccaagcagccttg gtcaggggtg gtagacgcta caaccttcca gagtgtctgc taccaatatg'
    sana4 = 'acgcacgccc gacgctggcc tgcgccggcc gctctcccac gcggggtctc gggggctcctgagccggccg cctccaggaa gcaggcgccg cgcggtattg ccgcatgcac ctcggtcgtggggaccccgc tgcagcagcc ctgtccacac gggtgaactc ctggagggcg gggcggggggcaatctgcgc gggtcaggcc cctcggagca ggctgggggc gcccgagcca ggccgctcccacctgccagc cgcgtggcca atgaatgcta ggcctggtga tgtcatgccc cgaccggaccctggtgacga aagtccgaag tcacccgtca gggaaccagc acagacccac ccgcgggggttccagaagtt tccactgccg ccgcggagtg cggcctcgcc cagcagcctt gcgcgtgcta'
    #ADN Anemias de células falciformes
    anemia1 = 'ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGTAaGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGC'
    anemia1_1 = 'atggaatcta cgttgacttt agcaacggaa caacctgtta agaagaacac tcttaagaaatataaaatag cttgcattgt tcttcttgct ttgctggtga tcatgtcact tggattaggcctggggcttg gactcaggaa actggaaaag caaggcagct gcaggaagaa gtgctttgatgcatcattta gaggactgga gaactgccgg tgtgatgtgg catgtaaaga ccgaggtgattgctgctggg attttgaaga cacctgtgtg gaatcaactc gaatatggat gtgcaataaatttcgttgtg gagagaccag attagaggcc agcctttgct cttgttcaga tgactgtttgcagaggaaag attgctgtgc tgactataag agtgtttgcc aaggagaaac ctcatggctg'
    anemia1_2 = 'atgagaggac ctgccgtcct gctgaccgtc gccctggcta ccttgctggc ccctggtgctggtgcaccca gctgcgccaa agaagtgaag tcctgcaagg gccggtgctt cgagcggaccttcggcaact gcagatgcga cgccgcctgt gtggaactgg gcaactgctg cctggactaccaggaaacct gcatcgagcc cgagcacatc tggacctgca acaagttcag atgcggcgagaagcggctga ccagatccct gtgtgcctgc agcgacgact gcaaggacaa gggcgactgctgcatcaact acagcagcgt gtgccagggc gagaagtcct gggtggaaga accctgcgagagcatcaacg agccccagtg ccctgccggc ttcgagacac ctcctaccct gctgttcagc'
    anemia1_3 = 'atgagaggac ctgccgtcct gctgaccgtc gccctggcta ccttgctggc ccctggtgctggtgcaccca gctgcgccaa agaagtgaag tcctgcaagg gccggtgctt cgagcggaccttcggcaact gcagatgcga cgccgcctgt gtggaactgg gcaactgctg cctggactaccaggaaacct gcatcgagcc cgagcacatc tggacctgca acaagttcag atgcggcgagaagcggctga ccagatccct gtgtgcctgc agcgacgact gcaaggacaa gggcgactgctgcatcaact acagcagcgt gtgccagggc gagaagtcct gggtggaaga accctgcgagagcatcaacg agccccagtg ccctgccggc ttcgagacac ctcctaccct gctgttcagc'
    anemia1_4 = 'atggaaaggg acggatgcgc cggtggtgga tctcgcggag gcgaaggtgg aagggcccctagggaaggac ctgccggaaa cggaagggac aggggacgct ctcacgccgc tgaagctccaggcgaccctc aggccgctgc ctctctgctg gctcctatgg acgtcggaga agaacccctggaaaaggccg ccagggccag gactgccaag gaccccaaca cctacaagat catctccctcttcactttcg ccgtcggagt caacatctgc ctgggattca ccgccggact gaagcccagctgcgccaaag aagtgaagtc ctgcaagggc cggtgcttcg agcggacctt cggcaactgcagatgcgacg ccgcctgtgt ggaactgggc aactgctgcc tggactacca ggaaacctgc'
    anemia1_5 = 'gacggatcgg gagatctccc gatcccctat ggtcgactct cagtacaatc tgctctgatgccgcatagtt aagccagtat ctgctccctg cttgtgtgtt ggaggtcgct gagtagtgcgcgagcaaaat ttaagctaca acaaggcaag gcttgaccga caattgcatg aagaatctgcttagggttag gcgttttgcg ctgcttcgcg atgtacgggc cagatatacg cgttgacattgattattgac tagttattaa tagtaatcaa ttacggggtc attagttcat agcccatatatggagttccg cgttacataa cttacggtaa atggcccgcc tggctgaccg cccaacgacccccgcccatt gacgtcaata atgacgtatg ttcccatagt aacgccaata gggactttcc'
    #ADN Anemias por deficiencia de hierro
    anemia2 = 'tgtatttcttccaatagtgactggcytttaggagccaattgatagaaaaat'
    anemia2_1 = 'attccttccc tcctggggtc tacacrcatt gctacggccc catcccagag c'
    anemia2_2 = 'aaaaattgtt agtcctttgt gttgartgaa taaatgaaat tgtgactgtg t'
    anemia2_3 = 'tgtatttctt ccaatagtga ctggcyttta ggagccaatt gatagaaaaa t'
    anemia2_4 = 'ctgagtttct agttttctct ggttgkgtgg gtcctcccca gctgtcaaat c'
    anemia2_5 = 'ggtgaaggac aaggctggtc tttccyctac cttgagttcc cagcaccccc a'
    anemia2_6 = 'atatcaaaat gcagtattcg caccaytgtg agcacctttt agagagactg a'
    anemia2_7 = 'atgtcctttg agcatcattt tttacyccca ttgggtgctt tacatttgtc t'
    #ADN Anemias megaloblástica
    anemia3 = 'actaaaaata caaaaattag ccaggtgtgg tggcacgcac ctgtaatccc agctattcgggaggctgagg caggagaatt gcttgaaccc aggaggttac agtgagcaga gattgaacccaggaggttac agtgagctga gattgcacaa gtgcactcca gcctgggtga cagagcgagagaccctatct caaaaaaaaa aaaagagggc aaaaagcatt cttaggaaaa ataaatgagctacaaaaagc ctctagaata aaaatcatag gtgctcattc agtgtttgta gacctaaaaa'
    anemia3_1 = 'atgggtctat gcagaataat caagcaatga aaggtaggct gccccagaat tgtaacattaaccgtggcaa attctctcaa gtcacgcctc cttgcatgac ccctccagaa aggtgaagttttagatttac ttttctcctt agccacacat ctccattcct gtagttattt catactaacactttcatgtt gaccctaaaa ttcaaatttt accttttatg gaaggattaa tattttacat'
    anemia3_2 = 'atatctccat tggacagata cctctatctg aattggaact tttttttttt ctcattctctttacctaatt tcctgaggat aatgaataaa gatggatttc ctgtcttccc ttatcacaaattctctggta ccataaaact agagaaaaat ctgctcaact gtctatatgc aacaccacctctagaaatcc aggaactcag gcactcaggc aggctgggtt tttatttatt tttgtgctgttttttgtttg ttttttgttt tgagacagag tctcgctttg ttgcccaggg tggagtgcag'
    anemia3_3 ='tggcacaatc ttggctcact gcaacctccg cctcctgggc tcaagtgatt ctcctgcctcaacctcccaa gtagctggga ttacaggcaa ctaccagcac gcccaactaa tttttgtatttttagtggag atgggatttc accatgttgg ccaggctggt cttaaactcc tgacctcaggtgatccacct gccttggcct cccaaagtgc tgagattaca ggtgtgagcc cctgcgcccagcctaggcat gctgttttta ttcaatgcct tttacataca caaagagcag ctctaagcaaaaaaaagcgg ggagagtaga tctgcaggtc ctgatactga aaattgttca aaattttcta'
    anemia3_4 ='ttaagtagaa aaagatagta gcaaattagt atagaatata atataatctg taaaatatatttaaactaat ttttgagctt atgactatgc acatatacac atgtacaaat ttttaaaatctggaagtata tacagaacac caatagcagt gggcctcact caaagggagg gattatggggtctatcactg cctaccttcc acatttctgt actgtttgaa atttctgtag caagaatgtt'
    anemia3_5 ='ttaattttat aaccaggaca aaaatagcta gaaggaataa aggagaaagt tgggagaactacagctaaat tgcagaattg tagctctacc atccccttaa cctcctatac acatcaccatcacctatagg gggccactct gctcaggaac aaaagggacc tttctccaca aagaaaaaagacacaattct aatacgctct tctgccctct ggagaattcc agaataccag agccatgactgaggagaaaa aagaatcccc cacaactcac cagagttgcc agacattccc agatcacttc'
    anemia3_6 = 'agcttc tttg ttgaga ccat ggcaga tcct tttgat gaag gcgccc aatg gtcgtg taatcctatggtgc ttgatgctta agttagtttt tgttattggt actttgatct attatacgta'
    anemia3_7 = 'gtcagcgctg tagtcggctc ggccctggaa gtaagatagc tatagcaccg gaagcttcatctaaaccagt agaacagctc gatagatata ttagtgggct tggaaatgaa ggcttagcgattagattttt acattcacga caatagcatt catgacgctg ctttggaaag cgaggttggg'
    anemia3_8 = 'tttggagacg ccgacactga tgacgacttc atgaggtacc gaaaaagtac acataagacccaaaatgagc acaggaaaga cgacacagga gttctcaagc tttccggtat gtttaacact'
    anemia3_9 = 'gtctttggct tattccctcc atttgtcagc atgcttctcg tactgtatga gagcctgacgaggagttcaa tcatcattgt ggactactgt gtgacagatg agtacccgac acagttgagggagctcgtcc aggtctacaa cgaagtcaag aagagctcgg acaatattgt gctcatgggt'
    anemia3_10 = 'gattctgctg gtgggcatct tgtgctaagt cttctaagac atgcggagca tccgttgacttcggtggaca cagtggtaat tgacaatgaa ttaaagggat tgatcttact ctcaccatgg'
    anemia3_11 = 'tgggatgtca tccatgtctg cagccttgat tgcgatctcg acagtcctta gcgtgccgcccttggcactc caaacttcaa acttgacaga gcggcctttg caattggata tctcctgctt'
    anemia3_12 = 'gaggtagtcg tagttgacac tgagctgata ctgatcatca tatgaggtag gcagctcgtggccattgatt ccgagaatga agtcgaacca gctctcaaga ccgacctctg ctgctgtaga'
    anemia3_13 = 'gtgaatcgtg tggtttgagc agaggcggca aaagtgggca aagccgaaca gggcaccttaacctttcccg ttttggacca gagttattag tgatgacgcg catgagctac caggtttccc'
    anemia3_14 = 'aggcacatgt tcagtgggtt ggtcaccagg tgtgggaata tcgatcaatt ctcaacataccagactcaca caatgggaag acaattgaac ttgttatgca tggtcttgac acattcgcagatgtctactt caatggctgt ttcatcaaga gcaccgataa tatgtttacc cggttcactcatccggttga gctacagaag ggcgataatg aaataagaat tcagttcaga tcagtgtttgaggttaaggt accctacgac cccgctgacc ttcaggaagg catcaaaagt agaatgtttg'

    if cadena in anemia1 or anemia1_1 or anemia1_2 or anemia1_3 or anemia1_4 or anemia1_5:
        print('el paciente tiene Anemia de células falciformes')
    elif cadena in(anemia2 or anemia2_1 or anemia2_2 or anemia2_3 or anemia2_4 or anemia2_5 or anemia2_6 or anemia2_7):
        print('el paciente tiene Anemia por deficiencia de hierro')
    elif cadena in (anemia3 or anemia3_1 or anemia3_2 or anemia3_3 or anemia3_4 or anemia3_5 or anemia3_6 or anemia3_7 or anemia3_8 or anemia3_9 or anemia3_10 or anemia3_11 or anemia3_12 or anemia3_13 or anemia3_14):
        print('el paciente tiene Anemia megaloblástica')
    elif cadena in (sana or sana1 or sana2 or sana3 or sana4):
        print('El paciente esta sano')
    else:
        print('No se puede verificar la cadena')

enfermedad()


