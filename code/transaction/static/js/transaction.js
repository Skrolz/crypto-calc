function createGrid(gridData) {
    console.log(gridData)
    const columnDefs = [{
            headerName: "Timestamp",
            field: "fields.timestamp",
            sort: 'asc',
            pinned: 'left'

        },
        {
            headerName: "Category",
            field: "fields.category"
        },
        {
            headerName: "Incoming Type",
            field: "fields.currency_in_type"
        },
        {
            headerName: "Incoming Quantity",
            field: "fields.currency_in_quantity",
            cellRenderer: function (params) {
                if (params.value) return parseFloat(params.value)
            }
        },
        {
            headerName: "Outgoing Type",
            field: "fields.currency_out_type"
        },
        {
            headerName: "Outgoing Quantity",
            field: "fields.currency_out_quantity",
            cellRenderer: function (params) {
                if (params.value) return parseFloat(params.value)
            }
        },
        {
            headerName: "Fee Type",
            field: "fields.fee_type"
        },
        {
            headerName: "Fee Quantity",
            field: "fields.fee_quantity",
            cellRenderer: function (params) {
                if (params.value) return parseFloat(params.value)
            },
        },
        {
            headerName: "Comments",
            field: "fields.comments",
            width: 800
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