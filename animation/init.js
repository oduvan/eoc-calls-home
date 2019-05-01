requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            functions: {
                js: 'totalCost',
                python: 'total_cost'
            }
        });
        io.start();
    }
);
