// config/auth.js

// expose our config directly to our application using module.exports
module.exports = {

    'facebookAuth' : {
        'clientID'      : '251768885289067', // your App ID
        'clientSecret'  : '69803b262211015ea714b2593e690e26', // your App Secret
        'callbackURL'   : 'https://stamps2-mknarciso.c9users.io:8080/auth/facebook/callback'
    }

};