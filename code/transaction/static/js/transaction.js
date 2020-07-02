function createGrid(gridData) {
    const columnDefs = [{
            headerName: "Timestamp",
            field: "fields.timestamp",
            sort: 'asc',
            pinned: 'left',
            cellRenderer: (params) => {
                return params.value.replace('Z', '').replace('T', ' -- ')
            }
        },
        {
            headerName: "Start",
            field: "fields.currency_in_quantity",
            cellRenderer: function (params) {
                if (params.value) return '<b>' + parseFloat(params.value) + '</b> - <i>' + params.data.fields.currency_in_type + '</i>'
            },
            cellStyle: {'text-align': 'right'}
        },
        {
            headerName: "Type",
            field: "fields.category",
            cellRenderer: (params) => {
                switch (params.value) {
                    case '1buy':
                        return '<b style="color:green">Buy</b>'                        
                    case '2sell':
                        return '<b style="color:red">Sell</b>'                        
                    case '3trade':
                        return '<b style="color:purple">Trade</b>'                        
                    case '4transfer':
                        return '<b style="color:grey">Transfer</b>'                        
                    case '5earn':
                        return '<b style="color:yellow">Earn</b>'
                    default:
                        return '-?-'
                }
            },
            cellStyle: {'text-align': 'center'}
        },
        {
            headerName: "End",
            field: "fields.currency_out_quantity",
            cellRenderer: function (params) {
                if (params.value) return '<i>' + params.data.fields.currency_out_type + '</i> - <b>' + parseFloat(params.value) + '</b>'
            }
        },
        {
            headerName: "Fee",
            field: "fields.fee_quantity",
            cellRenderer: function (params) {
                if (params.value) return '<i>' + params.data.fields.fee_type + '</i> - <b>' + parseFloat(params.value) + '</b>'
            }
        },
        {
            headerName: "Comments",
            field: "fields.comments",
            width: 800,
            cellStyle: {'font-style': 'italic'}
        },
    ];
    const rowData = gridData;
    let gridOptions = {
        columnDefs: columnDefs,
        defaultColDef: {
            sortable: true,
        },
        rowData: rowData,
    };
    document.addEventListener('DOMContentLoaded', function () {
        const gridDiv = document.querySelector('#transactions-grid');
        new agGrid.Grid(gridDiv, gridOptions);
    });
};