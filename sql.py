for i in range(1,123):
    print("insert into postgres.comtrade.comtrade\nselect *\nfrom postgres.comtrade.merged_data{};\n".format(str(i)))
    # print("alter table postgres.comtrade.merged_data{}\ndrop column \"netWgt\";\n".format(str(i)))
    # print("alter table postgres.comtrade.merged_data{}\ndrop column \"CIFValue\";\n".format(str(i)))
    # print("alter table comtrade.merged_data{}\n\talter column \"cmdCode\" type text using \"cmdCode\"::INT;\n".format(str(i)))