<script>
    import {goto} from "$app/navigation.js";
    import {Fileupload, Label, Button} from "flowbite-svelte";

    let file;

    function uploadFile() {
        // TODO
        console.log("POST", file);
        goto("/biopsy/id", {replaceState: false});
    }
</script>

<Label class="space-y-2 mb-2">
  <span>Upload DG file</span>
  <Fileupload bind:value={file} />
</Label>
<Label>File: {file ? file : "No file uploaded"}</Label>
<Button on:click={uploadFile}>Insert into database</Button>