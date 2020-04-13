function createGrid(gridData) {
    const columnDefs = [{
            headerName: "Timestamp",
            field: "fields.timestamp",
            sort: 'asc'
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
                return parseFloat(params.value)
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
                return parseFloat(params.value)
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
                return parseFloat(params.value)
            }
        },
    ];
    const rowData = gridData;
    let gridOptions = {
        columnDefs: columnDefs,
        rowData: rowData,
    };
    document.addEventListener('DOMContentLoaded', function () {
        const gridDiv = document.querySelector('#transactions-grid');
        new agGrid.Grid(gridDiv, gridOptions);
    });
};