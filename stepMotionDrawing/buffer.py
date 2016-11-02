
    #generateJsonFile(10)
    '''
    thread.Thread(testCase, (0,))
    thread.start_new_thread(generateJsonFile, (10,))
    threads = []
    t1 = threading.Thread(target=testCase,args=(0,))
    threads.append(t1)
    t2 = threading.Thread(target=generateJsonFile,args=(10,))
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    '''


    ''' trash
    if line[0] == 'L' and line[1] == '-':
        light_list_str = line.split(',')[1:-1]
        for e in light_list_str:
            light_list.append(float(e))

    if line[0] == 'S' and line[1] == '-':
        step_list = line.split(',')[1:-1]
    if line[0] == 'O' and line[1] == '-':
        orientation_list_str = line.split(',')[1:-1]
        for e in orientation_list_str:
                orientation_list.append(float(e))
    '''





    '''
    if startingDate is None:
        startingDate = 0
    if endingDate is None:
        endingDate = 1
    '''
 #assert os.path.exists(ele_file) == True
        assert os.path.exists(ele_file)
        '''
        if not os.path.exists(ele_file):
            print 0
            return
        else:
            print 1
        '''
