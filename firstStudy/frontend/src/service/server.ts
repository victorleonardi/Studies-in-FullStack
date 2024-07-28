import axios from 'axios'

export async function get_lib() {
  const resp = await axios.get('http://127.0.0.1:5000/games')
  return resp.data
}

export async function get_game(id: string) {
  const resp = await axios.get(`http://127.0.0.1:5000/games/${id}`)
  return resp.data
}

export async function add_game(payload: { name: string; genre: string; played: boolean }) {
  const resp = await axios.post(`http://127.0.0.1:5000/games`, payload)
  return resp.data
}

export async function delete_game(id: string) {
  const resp = await axios.delete(`http://127.0.0.1:5000/games/${id}`)
  return resp.data
}
