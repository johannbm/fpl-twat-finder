<script>
    import Entry from './Entry.svelte';
    export let leaugeId;

    $: fetchLeaugeStandings = (async (leaugeId) => {
        const response = await fetch(`/get-leauge-standings/${leaugeId}`);
        return await response.json()
    })(leaugeId)
</script>

<style>
    div {
        position: absolute;
    }
</style>

{#await fetchLeaugeStandings}
    <p>...waiting</p>
{:then standings}
    <p>The leauge has {standings.results.length} members</p>
    <div>
        {#each standings.results as entry}
            <Entry entry={entry} maxScore={standings.results[0].total}/>
        {/each}
    </div>
{/await}

