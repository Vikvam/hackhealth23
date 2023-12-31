<script type="module">
    import { onMount } from "svelte";
    import {SlickGrid, SlickDataView, SlickGridPager, SlickCellSelectionModel} from "slickgrid";

    export let tableId = "slickgrid";
    export let heightStyle = "500px"
    export let usePager = true;
    export let columns;
    export let rows;
    export let extraOptions = {};


    export let onCellChange = () => {};

    let grid;
    let dataView;

    let columnFilters = {};
    let options = {
        enableCellNavigation: true,
        enableColumnReorder: true,
        showHeaderRow: true,
        defaultColumnWidth: 160,
        rowHeight: 36,
        editable: true,

    };

    function filter(item) {
        for (let columnId in columnFilters) {
            if (columnId !== undefined && columnFilters[columnId] !== "") {
                let c = grid.getColumns()[grid.getColumnIndex(columnId)];
                let fieldValue = String(item[c.field]).toLowerCase(); // Convert to lowercase for case-insensitive comparison
                let filterValue = columnFilters[columnId].toLowerCase(); // Convert to lowercase for case-insensitive comparison

                if (!fieldValue.includes(filterValue)) {
                    return false;
                }
            }
        }
        return true;
    }

    function onHeaderRowChange(e) {
        const inputFilter = e.target;
        const parent = inputFilter.parentNode;
        const columnId = inputFilter.dataset.columnid;
        if (columnId != null) {
            columnFilters[columnId] = (e.target.value || "").trim();
            dataView.refresh();
            setTimeout(() => {
                parent.firstElementChild.focus();
            }, 10)
        }
    }

    function renderTable() {
        dataView = new SlickDataView({});
        grid = new SlickGrid(`#${tableId}`, dataView, columns, options);

        dataView.onRowCountChanged.subscribe(function (e, args) {
            grid.updateRowCount();
            grid.render();
        });

        dataView.onRowsChanged.subscribe(function (e, args) {
            //remove first row from args.rows
            grid.invalidateRows(args.rows);
            grid.render();
        });

        grid.onRendered.subscribe((e) => {
            let headerRow = grid.getHeaderRow();
            headerRow.addEventListener("change", onHeaderRowChange);
            headerRow.addEventListener("keyup", onHeaderRowChange);
            for (let i = 0; i < headerRow.children.length; i++) {
                const columnId = columns.at(i).id;
                const filterInput = document.createElement("input");
                filterInput.className = "filter";
                filterInput.placeholder = "Filter...";
                filterInput.dataset.columnid = columnId;
                filterInput.value = columnFilters[columnId] || "";
                const headerCell = headerRow.childNodes[i];
                headerCell.innerHTML = "";
                headerCell.appendChild(filterInput);
            }
        });

        grid.onCellChange.subscribe((e, args) => onCellChange(e, args));

        // grid.setSelectionModel(new SlickCellSelectionModel());

        grid.init();
        grid.setOptions({autoEdit: true, autoCommitEdit: true});

        let pager;
        if (usePager) {
            pager = new SlickGridPager(dataView, grid, `#${"pager" + tableId}`);
        }
        dataView.beginUpdate();
        dataView.setItems(rows);
        dataView.setFilter(filter);
        dataView.endUpdate();

        setTimeout(() => {
            grid.resizeCanvas();
        }, 10);
    }

    onMount(async () => {
        renderTable();
    });
</script>

<div class="table-container">
    <div id={tableId} style="width:100%;height:{heightStyle};" />
    {#if usePager}
        <div id={"pager" + tableId} style="width:100%;"></div>
    {/if}
</div>

<style>
    .table-container {
        width: 100%;
        /*margin: 2rem 0;*/
    }
</style>
