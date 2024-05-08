const APP_ID = 'a1ad6554f77d4a2381a06f974a42f05b'
const CHANNEL = 'rtc'
const TOKEN = '007eJxTYHiXe2vR9eM3arfnnlryr8U3PCWBZY9D1q7VZ+TZjV3qKn8oMCQaJqaYmZqapJmbp5gkGhlbGCYamKVZmpskmhilGZgmbcqxSGsIZGT4Pi+ImZEBAkF8ZoaikmQGBgDbnyDT'
let UID;


console.log('Streams Connected')


const client = AgoraRTC.createClient({mode: 'rtc', codec: 'vp8'})

let localTracks = []
let remoteUsers = {}


let joinAndDisplayLocalStream = async () => {
client.on('user-published', ()=>{
    console.log('User has joined our stream')
})

    UID = await client.join(APP_ID, CHANNEL, TOKEN, null) //This allows the user to join a channel
    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()  //This is going to take the user's video and audio track
    
    //This is going to represent each individual user in the stream with a unique identifire
    let player = `<div class="video-container" id="user-container-${UID}">              
                    <div class="username-wrapper"><span id="user-name">My name</span></div>
                    <div class = "video-player" id="user-${UID}"></div>
                </div>` 

    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

    localTracks[1].play(`user-${UID}`)

    await client.publish(localTracks[0], localTracks[1])
}


joinAndDisplayLocalStream()














//resources:
//https://docs.agora.io/en/video-calling/develop/integrate-token-generation?platform=android  -------Token Generation
// Documentation: https://docs.agora.io/en/api-reference?platform=web (video call api)
//https://www.youtube.com/watch?v=Oxnz8Us1QAQ&t=381s 47:40