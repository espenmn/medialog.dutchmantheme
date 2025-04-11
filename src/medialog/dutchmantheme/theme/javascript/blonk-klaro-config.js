window.klaroConfig = {
    privacyPolicy: '/privacy.html',
    styling: {
        theme: ['dark'], // Optional: sets light theme explicitly
    },
   services : [
        {
            name : 'google-analytics',
            default: false,
            title : 'Google Analytics',
            purposes : ['statistics'],
            cookies : [/^ga/i],
            callback : function(consent, app){
                // example callback
            },
        },
        {
            name: 'google-tag-manager',
            title: 'Google Tag Manager',
            purposes: ['marketing'],
            default: false,
            required: false,
            callback: function(consent, app) {
                if (consent) {
                    // Load GTM script
                    const gtmScript = document.createElement('script');
                    gtmScript.async = true;
                    gtmScript.src = 'https://www.googletagmanager.com/gtm.js?id=G-QTCSF2NY4G';
                    document.head.appendChild(gtmScript);

                    // Optionally add noscript fallback for non-JS environments
                    const noScript = document.createElement('noscript');
                    noScript.innerHTML = `<iframe src="https://www.googletagmanager.com/ns.html?id=G-QTCSF2NY4G" height="0" width="0" style="display:none;visibility:hidden"></iframe>`;
                    document.body.appendChild(noScript);
                }
            },
        },
        // Add more apps here if needed...
    ],
} 