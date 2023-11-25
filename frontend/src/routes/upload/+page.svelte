<script>
    import {goto} from "$app/navigation.js";
    import {Fileupload, Input, Label, Button, Heading} from "flowbite-svelte";

    let id;
    let file;

    function uploadFile() {
        // TODO
        console.log("POST", file);
        goto("/dg-edit", {replaceState: false});
    }
</script>

<div>
  <Heading tag="h3" class="space-y-10 mb-4">Insert new biopsy</Heading>
  <Label class="space-y-4 mb-4">
    <span>Biopsy ID</span>
    <Input bind:value={id} />
  </Label>
  <Label class="space-y-4 mb-4">
    <span>DG file</span>
    <Fileupload bind:value={file} />
  </Label>
  <Label class="space-y-4 mb-4">
    File: {file ? file : "No file uploaded"}
  </Label>
  <Button on:click={uploadFile}>Insert into database</Button>
</div>

<style>
  div {
    display: grid;
  }
  span {
    font-weight: bold;
  }
</style>