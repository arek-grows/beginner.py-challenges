import unittest
from typing import List


def missing_numbers(numbers: List[int]) -> List[int]:
    end_list = []
    if not numbers:
        return end_list
    numbers.sort()
    cu_nr = numbers[0] - 1
    for x in numbers:
        cu_nr += 1
        while cu_nr != x:
            end_list.append(cu_nr)
            cu_nr += 1
    return end_list  # Put your code here!!!


def missing_numbers_beta(numbers: List[int]) -> List[int]:
    end_list = []
    if not numbers:
        return end_list
    numbers.sort()
    for x in range(numbers[0], numbers[-1] + 1):
        if x not in numbers:
            end_list.append(x)
    return end_list  # Put your code here!!!


class TestMissingNum(unittest.TestCase):
    def test_1(self):
        self.assertEqual([5], missing_numbers([1, 2, 3, 4, 6, 7, 8, 9, 10]))

    def test_2(self):
        self.assertEqual([10], missing_numbers([7, 2, 3, 6, 5, 9, 1, 4, 11, 8]))

    def test_3(self):
        self.assertEqual([1, 8], missing_numbers([7, 2, 3, 9, 4, 5, 6, 10, 0]))

    def test_4(self):
        self.assertEqual([7], missing_numbers([10, 5, 1, 2, 4, 6, 8, 3, 9]))

    def test_5(self):
        self.assertEqual([3], missing_numbers([1, 7, 2, 4, 8, 10, 5, 6, 9]))

    def test_6(self):
        self.assertEqual([], missing_numbers([1, 2, 4, 3]))

    def test_7(self):
        self.assertEqual([], missing_numbers([]))

    def test_8(self):
        nums = [
            731,735,176,929,127,1001,60,285,214,750,1391,1396,1478,860,1319,495,154,921,1247,1260,301,1362,1489,242,538,
            775,1198,785,377,475,480,799,1295,992,473,711,464,1223,916,28,86,345,858,1054,535,456,1431,887,277,94,736,
            19,1006,207,234,384,877,938,900,1166,894,1076,1287,1157,455,903,478,1000,591,448,335,1016,1353,388,1445,789,
            80,956,95,441,578,1193,593,800,624,530,1386,639,1041,1316,740,616,1464,959,765,752,401,1397,1177,1361,524,
            230,64,994,156,1093,720,812,1473,1156,1466,774,821,1372,1108,525,1383,1049,1081,779,1008,969,997,611,1449,
            1330,453,469,1208,1475,1180,1032,428,984,832,445,490,613,426,1495,339,913,1169,830,895,1298,334,7,13,675,
            356,1018,270,1170,1030,1356,315,1444,224,366,582,71,239,1134,1048,444,866,1331,738,1114,1471,443,1448,1105,
            1265,440,836,855,49,22,18,193,1187,88,54,1299,1271,1220,632,1266,1080,1305,336,570,727,513,961,734,837,182,
            233,272,460,923,803,115,43,1410,1294,1389,952,283,1039,672,1190,347,864,1320,1199,108,34,132,1207,882,84,
            641,859,1409,187,195,706,660,29,810,1021,1371,296,413,1408,1070,138,1113,1446,1293,844,968,1455,1028,964,
            223,834,376,758,537,1462,761,302,1398,1335,92,311,768,813,1418,1332,562,385,905,486,320,850,363,1429,904,
            665,325,1339,128,1150,265,100,140,1077,1230,659,914,184,704,1145,1023,146,1254,1348,508,1273,1401,667,1194,
            857,1014,1468,57,498,550,1301,622,1322,1491,391,280,429,1167,804,23,983,573,1140,1341,1343,1480,1218,46,
            1428,405,158,1110,180,863,522,167,364,1250,470,97,15,161,1284,636,422,702,281,113,1239,386,1476,865,8,1474,
            5,1278,179,82,802,1042,1192,53,178,489,365,333,504,1358,712,423,1314,572,190,816,1184,528,1487,90,1382,794,
            892,605,1481,653,9,1065,1465,482,840,343,1159,491,397,317,872,109,554,1209,829,367,754,205,920,1264,374,
            1267,400,1400,909,1394,847,1346,256,1204,406,341,477,1020,434,598,643,258,255,368,678,119,509,1029,228,185,
            808,1138,420,699,728,402,748,826,106,200,1213,967,1436,1133,719,1291,1191,776,72,777,651,1364,1205,410,737,
            412,1385,932,449,1176,681,546,796,527,373,324,1380,548,1004,1165,1128,316,1393,620,691,1423,220,907,685,
            1123,1384,1318,414,1100,1124,991,226,1129,849,271,977,1482,181,1117,1453,663,278,416,463,105,1034,133,1242,
            949,868,348,1225,1252,273,297,756,1005,331,792,1402,73,881,1373,679,163,797,536,1212,26,501,1163,33,1089,
            357,551,604,17,896,574,950,1430,906,1470,1439,1285,517,910,1109,465,730,1052,1037,841,44,493,299,683,263,
            933,539,1097,649,908,1038,149,16,922,1399,729,1344,749,941,338,507,766,982,772,284,1227,1211,888,975,248,
            709,1147,873,1454,559,1411,1106,782,1311,120,1337,695,886,1091,928,411,936,371,558,948,1181,1216,352,1276,
            170,842,186,721,788,1146,1068,516,817,432,1055,144,1338,1486,328,1121,541,618,724,55,1281,1098,569,851,1095,
            1375,786,1013,552,931,250,725,459,344,431,723,741,597,534,1424,838,390,136,827,1280,1051,795,203,655,107,
            1025,1351,1182,1210,743,439,1090,1499,1161,358,1059,1130,1088,854,11,1483,1045,74,118,798,483,746,349,599,
            883,217,101,673,688,1142,42,404,25,91,249,759,1370,104,1099,1072,56,66,1031,372,1186,862,561,481,329,48,823,
            1107,1085,1456,814,658,1258,540,549,1063,686,103,1234,1010,716,544,778,206,395,232,286,781,710,575,953,891,
            1,1329,925,1035,878,912,1139,1415,1365,312,394,261,172,322,564,337,1443,274,556,852,1477,243,707,612,511,31,
            474,75,647,708,351,1262,216,1078,383,790,502,965,79,603,617,236,1243,848,1238,880,762,560,398,269,1119,61,
            629,1312,1261,424,680,543,974,382,1116,1479,305,1417,621,12,586,1442,677,979,584,279,981,506,811,656,520,
            976,633,947,415,1306,246,452,822,588,1307,162,963,1325,457,407,1087,126,1275,592,1084,769,442,1406,742,973,
            310,164,387,770,59,833,590,791,1441,532,295,139,1342,690,631,51,990,571,454,1206,1421,1151,63,694,110,1062,
            1340,1120,1002,1321,359,962,619,58,1179,124,1033,476,177,1214,175,625,870,601,989,1125,1036,1111,1057,145,
            1224,1071,666,21,1484,253,1183,682,326,946,1189,1046,1155,116,294,142,290,1067,806,208,1363,637,112,780,446,
            783,1447,479,275,215,1011,467,940,1101,1079,497,1226,494,805,644,897,1422,499,503,244,27,221,835,1432,1137,
            1440,36,123,212,247,657,211,148,2,697,1498,615,378,121,435,579,1256,39,971,1381,1392,313,875,160,462,1222,
            958,1472,227,917,93,986,40,319,1047,567,427,209,1359,83,955,245,1286,419,436,1414,471,771,1437,646,1162,484,
            102,1317,1349,314,408,853,824,174,437,1494,135,846,1009,1053,425,767,157,468,1064,266,1326,510,1461,960,231,
            1185,957,1259,213,784,661,1231,670,1492,1467,614,1327,1355,939,191,1203,1148,607,757,461,392,451,995,1374,
            1050,640,623,924,1457,362,257,705,152,1255,1073,125,150,303,264,438,696,1297,96,1228,1387,1350,1171,1158,
            587,188,1012,674,433,1366,1143,609,1274,988,225,874,845,1303,131,545,1026,1082,1132,1195,671,1336,1412,1463,
            818,996,828,192,1056,576,884,1015,141,843,820,1175,869,602,515,1215,1245,1141,555,1279,600,652,1074,1469,
            458,687,902,1427,298,1017,1202,1236,287,505,1404,1407,1024,1347,1333,1302,466,370,1497,147,1300,521,1270,
            596,418,111,238,553,1309,1173,945,627,1201,985,751,1244,531,1136,1069,45,379,52,304,20,399,698,1304,951,676,
            129,375,1289,568,856,668,41,198,1027,1413,308,1153,1112,450,1292,309,1310,50,942,6,1277,512,1102,861,1019,
            606,1419,1268,703,1360,1251,1152,421,99,580,526,68,1452,760,1368,557,430,787,130,1188,954,47,24,934,65,889,
            1086,1241,944,81,1367,30,793,744,972,839,518,1378,35,1420,259,1354,867,1388,930,340,739,389,288,201,993,
            1232,1160,276,380,37,662,1240,714,254,876,292,488,664,219,492,589,500,1269,143,577,1433,237,202,1390,260,
            642,171,533,252,1248,1075,199,918,3,819,251,1323,1022,879,1219,1490,638,581,262,1290,332,403,173,1164,166,
            165,1249,654,1200,978,1296,1172,417,487,1040,1043,1272,911,1345,684,1196,701,871,650,529,14,1315,0,240,1379,
            241,1352,885,927,32,1217,1313,1253,594,1288,114,153,547,935,542,1135,1066,137,722,355,1118,38,10,1168,700,
            1416,1246,346,318,1144,1334,168,669,634,1485,1257,713,151,330,1060,134,717,1493,1328,472,4,268,1426,1263,
            919,898,1096,361,183,628,222,635,1092,1450,447,1154,1174,267,1357,901,733,1435,899,773,1369,610,1459,155,
            1094,1221,1308,1458,809,1007,393,1324,747,583,689,1283,745,1127,229,496,98,1131,630,360,196,353,937,1058,
            815,980,204,1460,626,1233
        ]
        missing = [
            62,67,69,70,76,77,78,85,87,89,117,122,159,169,189,194,197,210,218,235,282,289,291,293,300,306,307,321,323,
            327,342,350,354,369,381,396,409,485,514,519,523,563,565,566,585,595,608,645,648,692,693,715,718,726,732,753,
            755,763,764,801,807,825,831,890,893,915,926,943,966,970,987,998,999,1003,1044,1061,1083,1103,1104,1115,1122,
            1126,1149,1178,1197,1229,1235,1237,1282,1376,1377,1395,1403,1405,1425,1434,1438,1451,1488,1496
        ]
        self.assertEqual(missing, missing_numbers(nums))


if __name__ == "__main__":
    unittest.main()