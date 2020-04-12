function createGrid(gridData) {
    const columnDefs = [{
            headerName: "Abbreviation",
            field: "fields.abbreviation",
            sort: 'asc'
        },
        {
            headerName: "Name",
            field: "fields.name"
        },
        {
            headerName: "Comments",
            field: "fields.comments",
            width: 500
        }
    ];
    const rowData = gridData;
    let gridOptions = {
        columnDefs: columnDefs,
        rowData: rowData
    };
    document.addEventListener('DOMContentLoaded', function () {
        const gridDiv = document.querySelector('#currencies-grid');
        new agGrid.Grid(gridDiv, gridOptions);
    });
}