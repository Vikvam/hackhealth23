import {writable, derived} from 'svelte/store';

export const width = writable(0);

export const device = derived([width], ([width]) => {
    if (width < 500) { return 'mobile'; }
    else if (width < 1100) { return 'tablet'; }
    else { return 'desktop'; }
    // if (width > 1000) { return 'desktop'; }
    // else if (width > 800) { return 'tablet'; }
    // else { return 'mobile'; }
});