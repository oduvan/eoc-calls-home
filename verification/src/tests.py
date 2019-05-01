"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ("2014-01-01 01:12:13 181",
                      "2014-01-02 20:11:10 600",
                      "2014-01-03 01:12:13 6009",
                      "2014-01-03 12:13:55 200"),
            "answer": 124,
        },
        {
            "input": ("2014-02-05 01:00:00 1",
                      "2014-02-05 02:00:00 1",
                      "2014-02-05 03:00:00 1",
                      "2014-02-05 04:00:00 1"),
            "answer": 4,
        },
        {
            "input": ("2014-02-05 01:00:00 60",
                      "2014-02-05 02:00:00 60",
                      "2014-02-05 03:00:00 60",
                      "2014-02-05 04:00:00 6000"),
            "answer": 106,
        }

    ],
    "Edge": [
        {
            "input": ['2055-09-09 12:00:00 7200'],
            "answer": 140},

        {
            "input": ['2055-09-09 12:00:00 1'],
            "answer": 1},

        {
            "input": ['2051-09-09 12:00:00 1', '2051-09-10 12:00:00 1', '2051-09-12 12:00:00 1',
                      '2051-09-14 12:00:00 1', '2051-09-15 12:00:00 1', '2051-09-18 12:00:00 1',
                      '2051-09-23 12:00:00 1', '2051-09-25 12:00:00 1', '2051-09-28 12:00:00 1',
                      '2051-10-01 12:00:00 1', '2051-10-02 12:00:00 1', '2051-10-04 12:00:00 1',
                      '2051-10-05 12:00:00 1', '2051-10-06 12:00:00 1', '2051-10-07 12:00:00 1',
                      '2051-10-08 12:00:00 1', '2051-10-09 12:00:00 1', '2051-10-10 12:00:00 1',
                      '2051-10-11 12:00:00 1', '2051-10-12 12:00:00 1', '2051-10-13 12:00:00 1',
                      '2051-10-14 12:00:00 1', '2051-10-15 12:00:00 1', '2051-10-16 12:00:00 1',
                      '2051-10-17 12:00:00 1', '2051-10-18 12:00:00 1', '2051-10-19 12:00:00 1',
                      '2051-10-20 12:00:00 1', '2051-10-21 12:00:00 1', '2051-10-22 12:00:00 1'],
            "answer": 30},

        {
            "input": ['2051-09-09 12:00:00 7200', '2051-09-10 12:00:00 7200', '2051-09-12 12:00:00 7200',
                      '2051-09-14 12:00:00 7200', '2051-09-15 12:00:00 7200', '2051-09-18 12:00:00 7200',
                      '2051-09-23 12:00:00 7200', '2051-09-25 12:00:00 7200', '2051-09-28 12:00:00 7200',
                      '2051-10-01 12:00:00 7200', '2051-10-02 12:00:00 7200', '2051-10-04 12:00:00 7200',
                      '2051-10-05 12:00:00 7200', '2051-10-06 12:00:00 7200', '2051-10-07 12:00:00 7200',
                      '2051-10-08 12:00:00 7200', '2051-10-09 12:00:00 7200', '2051-10-10 12:00:00 7200',
                      '2051-10-11 12:00:00 7200', '2051-10-12 12:00:00 7200', '2051-10-13 12:00:00 7200',
                      '2051-10-14 12:00:00 7200', '2051-10-15 12:00:00 7200', '2051-10-16 12:00:00 7200',
                      '2051-10-17 12:00:00 7200', '2051-10-18 12:00:00 7200', '2051-10-19 12:00:00 7200',
                      '2051-10-20 12:00:00 7200', '2051-10-21 12:00:00 7200', '2051-10-22 12:00:00 7200'],
            "answer": 4200},

        {
            "input": ['2057-01-01 00:00:00 7200', '2057-01-01 03:00:00 7200', '2057-01-01 06:00:00 7200',
                      '2057-01-01 09:00:00 7200', '2057-01-01 12:00:00 7200', '2057-01-01 15:00:00 7200',
                      '2057-01-01 18:00:00 7200', '2057-01-01 21:00:00 7200', '2057-01-01 23:10:00 7200'],
            "answer": 2060},
    ],
    "Extra": [
        {
            "input": ['2054-07-17 10:21:08 1958', '2054-07-17 16:17:18 1388', '2054-07-18 00:30:57 729',
                      '2054-07-18 03:55:30 4970', '2054-07-18 23:10:05 5397', '2054-07-19 16:37:31 5894',
                      '2054-07-20 11:21:10 2537', '2054-07-20 17:09:49 4398', '2054-07-21 04:17:34 2839',
                      '2054-07-21 06:23:25 6229', '2054-07-21 10:21:01 4540', '2054-07-21 22:10:46 5599',
                      '2054-07-22 11:26:43 6199', '2054-07-23 02:02:52 818', '2054-07-23 14:30:19 3244',
                      '2054-07-23 20:46:25 380', '2054-07-24 08:41:40 4774', '2054-07-24 23:33:14 5206',
                      '2054-07-25 08:47:44 3848', '2054-07-25 11:32:40 694', '2054-07-25 18:28:25 5974',
                      '2054-07-26 09:24:52 4550', '2054-07-26 13:06:07 6637', '2054-07-27 09:03:40 177',
                      '2054-07-27 13:11:42 5736', '2054-07-27 15:53:26 5698', '2054-07-28 09:51:43 1996',
                      '2054-07-28 14:03:30 432'],
            "answer": 2382},

        {
            "input": ['2018-07-20 15:09:15 4580', '2018-07-21 10:52:17 3445', '2018-07-21 13:18:00 6630',
                      '2018-07-21 23:14:26 6165', '2018-07-22 11:17:02 1817'],
            "answer": 552},

        {
            "input": ['2064-11-08 09:25:18 3571', '2064-11-08 17:37:03 2921', '2064-11-08 20:37:07 2478',
                      '2064-11-09 04:55:03 6337', '2064-11-09 17:45:54 5727', '2064-11-09 21:50:44 23',
                      '2064-11-10 15:09:09 2709'],
            "answer": 554},

        {
            "input": ['2041-10-21 18:05:37 1464'],
            "answer": 25},

        {
            "input": ['2090-08-17 10:33:35 4711', '2090-08-18 05:22:04 2825', '2090-08-18 13:37:38 3447',
                      '2090-08-18 17:03:24 3070', '2090-08-18 21:41:35 951'],
            "answer": 327},

        {
            "input": ['2080-09-03 06:28:54 748', '2080-09-03 16:04:49 5930', '2080-09-04 06:15:17 4091',
                      '2080-09-04 14:34:14 6409', '2080-09-05 03:53:29 5578', '2080-09-05 07:35:07 4222',
                      '2080-09-05 16:50:55 3776', '2080-09-06 04:42:18 920'],
            "answer": 746},

        {
            "input": ['2091-07-20 14:19:07 763', '2091-07-21 03:01:05 2438', '2091-07-21 12:38:10 4461',
                      '2091-07-21 17:07:49 4234', '2091-07-22 13:05:43 1822', '2091-07-23 04:59:58 5656',
                      '2091-07-23 13:00:28 4273', '2091-07-24 03:52:59 3725', '2091-07-24 14:08:46 1728',
                      '2091-07-25 06:35:06 4518', '2091-07-25 18:32:17 386', '2091-07-26 03:52:46 3377',
                      '2091-07-26 18:32:49 39', '2091-07-27 00:04:11 3714', '2091-07-27 05:06:37 6908'],
            "answer": 1041},

        {
            "input": ['2074-01-20 14:22:43 2020', '2074-01-20 23:53:37 2918', '2074-01-21 07:38:23 713',
                      '2074-01-21 19:19:09 378', '2074-01-22 09:04:46 3954', '2074-01-22 17:19:51 5900',
                      '2074-01-23 04:21:00 788', '2074-01-23 18:09:30 784', '2074-01-24 04:11:41 6549',
                      '2074-01-24 16:22:06 1050', '2074-01-25 11:17:57 6986', '2074-01-26 00:48:52 4907',
                      '2074-01-26 19:58:59 6343', '2074-01-27 00:44:46 3040', '2074-01-27 07:10:20 4782',
                      '2074-01-28 01:22:59 1997', '2074-01-28 04:09:38 839'],
            "answer": 1136},

        {
            "input": ['2033-10-04 15:48:32 5909', '2033-10-04 20:39:39 6339', '2033-10-05 01:21:21 6035',
                      '2033-10-05 08:12:00 782', '2033-10-05 20:02:09 2187', '2033-10-06 10:47:42 2484',
                      '2033-10-07 00:17:35 6519', '2033-10-07 08:07:41 4832', '2033-10-07 12:20:56 2170',
                      '2033-10-08 03:58:26 5637', '2033-10-08 14:14:50 3645', '2033-10-09 07:34:44 4382',
                      '2033-10-09 10:29:25 4901', '2033-10-09 15:13:36 3105', '2033-10-10 10:20:54 6579',
                      '2033-10-10 22:51:17 1881', '2033-10-11 13:08:15 2548', '2033-10-11 16:02:44 1539',
                      '2033-10-12 06:42:35 3151'],
            "answer": 1742},

        {
            "input": ['2049-05-03 09:08:46 1965', '2049-05-03 20:23:02 1247', '2049-05-04 05:07:07 5836',
                      '2049-05-05 00:34:45 4387', '2049-05-05 05:08:49 4061', '2049-05-05 12:26:56 4831',
                      '2049-05-06 01:25:26 2570', '2049-05-06 19:36:49 3980', '2049-05-07 14:43:38 3308',
                      '2049-05-07 23:16:11 2181', '2049-05-08 04:41:29 461', '2049-05-08 14:28:42 2018',
                      '2049-05-09 08:50:59 1036', '2049-05-10 00:55:33 3498', '2049-05-10 16:22:12 4458',
                      '2049-05-11 07:54:22 2715', '2049-05-12 00:45:18 353', '2049-05-12 12:55:36 3836',
                      '2049-05-13 00:57:10 4515', '2049-05-13 19:18:07 2274'],
            "answer": 1183},
    ]
}
