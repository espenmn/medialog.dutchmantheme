/*
By default, Klaro will load the config from a global 'klaroConfig' variable. You
can change this by specifying the 'data-klaro-config' attribute on your script:
<script src="klaro.js" data-klaro-config="myConfigVariableName"
*/
var klaroConfig = {
    /*
    Setting 'testing' to 'true' will cause Klaro to not show the consent notice or
    modal by default, except if a special hash tag is appended to the URL (#klaro-
    testing). This makes it possible to test Klaro on your live website without
    affecting normal visitors.
    */
    testing: false,

    /*
    You can customize the ID of the DIV element that Klaro will create when starting
    up. By default, Klaro will use 'klaro'.
    */
    elementID: 'klaro',

    /*
    You can customize how Klaro persists consent information in the browser. Specify
    either cookie' (the default) or 'localStorage'.
    */
    storageMethod: 'cookie',

    /*
    You can customize the name of the cookie or localStorage entry that Klaro will
    use for storing the consent information. By default, Klaro will use 'klaro'.
    */
    storageName: 'klaro',

    /*
    If set to `true`, Klaro will render the texts given in the
    `consentModal.description` and `consentNotice.description` translations as HTML.
    This enables you to e.g. add custom links or interactive content.
    */
    htmlTexts: false,

    /*
    You can change the cookie domain for the consent manager itself. Use this if you
    want to get consent once for multiple matching domains. By default, Klaro will
    use the current domain. Only relevant if 'storageMethod' is set to 'cookie'.
    */
    cookieDomain: '.example.com',

    /*
    You can also set a custom expiration time for the Klaro cookie. By default, it
    will expire after 30 days. Only relevant if 'storageMethod' is set to 'cookie'.
    */
    cookieExpiresAfterDays: 30,

    /*
    Defines the default state for services in the consent modal (true=enabled by
    default). You can override this setting in each service.
    */
    default: false,

    /*
    If 'mustConsent' is set to 'true', Klaro will directly display the consent
    manager modal and not allow the user to close it before having actively
    consented or declined the use of third-party services.
    */
    mustConsent: false,

    /*
    Setting 'acceptAll' to 'true' will show an "accept all" button in the notice and
    modal, which will enable all third-party services if the user clicks on it. If
    set to 'false', there will be an "accept" button that will only enable the
    services that are enabled in the consent modal.
    */
    acceptAll: true,

    /*
    Setting 'hideDeclineAll' to 'true' will hide the "decline" button in the consent
    modal and force the user to open the modal in order to change his/her consent or
    disable all third-party services. We strongly advise you to not use this
    feature, as it opposes the "privacy by default" and "privacy by design"
    principles of the GDPR (but might be acceptable in other legislations such as
    under the CCPA)
    */
    hideDeclineAll: false,

    /*
    Setting 'hideLearnMore' to 'true' will hide the "learn more / customize" link in
    the consent notice. We strongly advise against using this under most
    circumstances, as it keeps the user from customizing his/her consent choices.
    */
    hideLearnMore: false,

    /*
    You can overwrite existing translations and add translations for your service
    descriptions and purposes. See `src/translations/` for a full list of
    translations that can be overwritten:
    https://github.com/KIProtect/klaro/tree/master/src/translations
    */
    translations: {
        /*
        The `zz` key contains default translations that will be used as fallback values.
            This can e.g. be useful for defining a fallback privacy policy URL.
        */
        zz: {
            privacyPolicyUrl: '/privacy',

        }
        de: {
            /*
            You can specify a language-specific link to your privacy policy here.
            */
            privacyPolicyUrl: '/datenschutz',
            consentNotice: {
                description: 'Dieser Text wird in der Einwilligungsbox erscheinen.',
            },
            consentModal: {
                description:
                    'Hier können Sie einsehen und anpassen, welche Information wir über Sie ' + 
                    'sammeln. Einträge die als "Beispiel" gekennzeichnet sind dienen lediglich ' + 
                    'zu Demonstrationszwecken und werden nicht wirklich verwendet.',
            },
            /*
            You should also define translations for every purpose you define in the
            'services' section. You can define a title and an (optional) description.
            */
            purposes: {
                analytics: {
                    title: 'Besucher-Statistiken'
                },
                security: {
                    title: 'Sicherheit'
                },
                livechat: {
                    title: 'Live Chat'
                },
                advertising: {
                    title: 'Anzeigen von Werbung'
                },
                styling: {
                    title: 'Styling'
                },
            },
        },
        en: {
            privacyPolicyUrl: '/privacy',
            consentModal: {
                description:
                    'Here you can see and customize the information that we collect about you. ' + 
                    'Entries marked as "Example" are just for demonstration purposes and are not ' + 
                    'really used on this website.',
            },
            purposes: {
                analytics: {
                    title: 'Analytics'
                },
                security: {
                    title: 'Security'
                },
                livechat: {
                    title: 'Livechat'
                },
                advertising: {
                    title: 'Advertising'
                },
                styling: {
                    title: 'Styling'
                },
            },
        },
    },

    /*
    Here you specify the third-party services that Klaro will manage for you.
    */
    services: [
        {

            /*
            Each service must have a unique name. Klaro will look for HTML elements with a
            matching 'data-name' attribute to identify elements that belong to this service.
            */
            name: 'matomo',

            /*
            If 'default' is set to 'true', the service will be enabled by default. This
            overrides the global 'default' setting.
            */
            default: true,

            /*
            Translations belonging to this service go here. The key `zz` contains default
            translations that will be used as a fallback if there are no translations
            defined for a given language.
            */
            translations: {
                zz: {
                    title: 'Matomo/Piwik'
                },
                en: {
                    description: 'Matomo is a simple, self-hosted analytics service.'
                },
                de: {
                    description: 'Matomo ist ein einfacher, selbstgehosteter Analytics-Service.'
                },
            },
            /*
            The purpose(s) of this service that will be listed on the consent notice. Do not
            forget to add translations for all purposes you list here.
            */
            purposes: ['analytics'],

            cookies: [
                /*
                you an either only provide a cookie name or regular expression (regex) or a list
                consisting of a name or regex, a path and a cookie domain. Providing a path and
                domain is necessary if you have services that set cookies for a path that is not
                "/", or a domain that is not the current domain. If you do not set these values
                properly, the cookie can't be deleted by Klaro, as there is no way to access the
                path or domain of a cookie in JS. Notice that it is not possible to delete
                cookies that were set on a third-party domain, or cookies that have the HTTPOnly
                attribute: https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie#new-
                cookie_domain
                */

                /*
                This rule will match cookies that contain the string '_pk_' and that are set on
                the path '/' and the domain 'klaro.kiprotect.com'
                */
                [/^_pk_.*$/, '/', 'klaro.kiprotect.com'],

                /*
                Same as above, only for the 'localhost' domain
                */
                [/^_pk_.*$/, '/', 'localhost'],

                /*
                This rule will match all cookies named 'piwik_ignore' that are set on the path
                '/' on the current domain
                */
                'piwik_ignore',
            ],

            /*
            You can define an optional callback function that will be called each time the
            consent state for the given service changes. The consent value will be passed as
            the first parameter to the function (true=consented). The `service` config will
            be passed as the second parameter.
            */
            callback: function(consent, service) {
                console.log(
                    'User consent for service ' + service.name + ': consent=' + consent
                );
            },

            /*
            If 'required' is set to 'true', Klaro will not allow this service to be disabled
            by the user. Use this for services that are always required for your website to
            function (e.g. shopping cart cookies).
            */
            required: false,

            /*
            If 'optOut' is set to 'true', Klaro will load this service even before the user
            has given explicit consent. We strongly advise against this.
            */
            optOut: false,

            /*
            If 'onlyOnce' is set to 'true', the service will only be executed once
            regardless how often the user toggles it on and off. This is relevant e.g. for
            tracking scripts that would generate new page view events every time Klaro
            disables and re-enables them due to a consent change by the user.
            */
            onlyOnce: true,
        },
        {
            name: 'youtube',
            /*
            [no translation for key annotated-config.services.contextualConsentOnly]
            */
            contextualConsentOnly: true,
        },
    ],

    /*
    You can define an optional callback function that will be called each time the
    consent state for any given service changes. The consent value will be passed as
    the first parameter to the function (true=consented). The `service` config will
    be passed as the second parameter.
    */
    callback: function(consent, service) {
        console.log(
            'User consent for service ' + service.name + ': consent=' + consent
        );
    },

};