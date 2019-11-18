import Vue from 'vue'

export const EventBus = new Vue()

export function isValidJwt (jwt) {
    if (!jwt || jwt.split('.').length < 3) {
        return false
    }
    const data = JSON.parse(atob(jwt.split('.')[1]))
    const exp = new Date(data.exp * 3000) // js deals in miliseconds
    const now = new Date()
    return now < exp
}


// EXAMPLE
// const token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJleGFtcGxlQG1haWwuY29tIiwiaWF0IjoxNTIyMzI2NzMyLCJleHAiOjE1MjIzMjg1MzJ9.1n9fx0vL9GumDGatwm2vfUqQl3yZ7Kl4t5NWMvW-pgw'
// const tokenParts = token.split('.')
// const body = JSON.parse(atob(tokenParts[1]))
// console.log(body)   // {sub: "example@mail.com", iat: 1522326732, exp: 1522328532}