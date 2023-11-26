<script>
    import { onMount } from "svelte";
    import Table from "$lib/components/Table.svelte";
    import Chart from "chart.js/auto";

    let mounted = false;
    let columnsGeneDanger = [];
    let rowsGeneDanger = [];
    let columnsMutationTypeDanger = [];
    let rowsMutationTypeDanger = [];

    async function fetchGeneDangerData() {
        const response = await fetch("http://localhost:8000/geneDanger");
        if (response.status > 400) {
            console.log("ERR"); // TODO
            return;
        }
        return response.json();
    }

    async function fetchMutationTypeDangerData() {
        const response = await fetch("http://localhost:8000/mutationTypeDanger");
        if (response.status > 400) {
            console.log("ERR"); // TODO
            return;
        }
        return response.json();
    }

    function linkFormatter(row, cell, value, columnDef, dataContext) {
        console.log(value);
        return (
            "<a style='color: blue; text-decoration: underline' href='https://www.genecards.org/Search/Keyword?queryString=" +
            value +
            "' target='_blank'>" +
            value +
            "</a>"
        );
    }

    onMount(async () => {
        columnsGeneDanger = [
            { id: "name", name: "Gene", field: "name", formatter: linkFormatter },
            { id: "n_safe", name: "# Pathogenic", field: "n_safe" },
            { id: "n_dangerous", name: "# Benign", field: "n_dangerous" },
            { id: "freq", name: "% Freq", field: "freq" },
        ];
        rowsGeneDanger = await fetchGeneDangerData();
        mounted = true;


        columnsMutationTypeDanger = [
            { id: "mutation_type", name: "Mutation Type", field: "mutation_type" },
            { id: "n_safe", name: "# Pathogenic", field: "n_safe" },
            { id: "n_dangerous", name: "# Benign", field: "n_dangerous" },
            { id: "freq", name: "% Freq", field: "freq" },
        ];
        rowsMutationTypeDanger = await fetchMutationTypeDangerData();
        console.log(rowsMutationTypeDanger)
        mounted = true;

        setTimeout(() => {
            const ctx = document
                .getElementById("circularChart")
                .getContext("2d");

            const totalGenes = rowsGeneDanger.reduce(
                (total, gene) => total + gene.n_safe + gene.n_dangerous,
                0
            );
            const dangerousGenes = rowsGeneDanger.reduce(
                (total, gene) => total + gene.n_dangerous,
                0
            );
            const safeGenes = totalGenes - dangerousGenes;

            console.log("chart", totalGenes, dangerousGenes);

            const chartData = {
                labels: ["Dangerous Genes", "Safe Genes"],
                datasets: [
                    {
                        data: [dangerousGenes, safeGenes],
                        backgroundColor: ["#FF6384", "#36A2EB"],
                    },
                ],
            };

            new Chart(ctx, {
                type: "doughnut",
                data: chartData,
            });
        }, 50);
    });
</script>

{#if mounted}
    <div class="grid-container">
        <div>
            <Table
                tableId="table1"
                columns={columnsGeneDanger}
                rows={rowsGeneDanger}
                options={{ defaultColumnWidth: 30 }}
                heightStyle="350px"
                usePager={true}
            />
        </div>

        <div><canvas id="circularChart" width="150" height="150" /></div>

        <div>
            <Table
                tableId="table3"
                columns={columnsMutationTypeDanger}
                rows={rowsMutationTypeDanger}
                heightStyle="200px"
                usePager={true}
            />
        </div>
    </div>
{/if}

<style>
    .grid-container {
        display: grid;
        grid-template-columns: auto auto auto; /* Adjust this to change the number of columns */
        gap: 10px; /* Adjust this to change the gap between the grid items */
        padding: 10px; /* Adjust this to change the padding around the grid */
        width: 100%;
    }

    .grid-container > div {
        background-color: #f1f1f1;
        width: 100%;
    }

    canvas {
        max-height: 300px !important;
        max-width: 300px !important;
        width: 100% !important;
        height: 100% !important;
        display: block;
        margin: auto;
    }
</style>
