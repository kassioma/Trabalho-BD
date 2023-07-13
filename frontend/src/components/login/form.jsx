import { React, useState } from "react";

export default function LoginForm() {
  const [matricula, setMatricula] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirm, setPasswordConfirm] = useState("");
  const [curso, setCurso] = useState("");
  const [imagem, setImagem] = useState(null);
  const [nome, setNome] = useState("");
  
  const submitForm = async () => {
    const formData = new FormData()
    formData.append('file', imagem)
    const responseUser = await fetch('http://localhost:8000/Usuarios/criar-usuario',{
      method: "POST",
      body: JSON.stringify({
        matricula: matricula,
        email: email,
        senha: password,
        curso: curso,
        nome: nome,
        admin: 0
      }),
      headers: {
        'content-type': 'application/json'
      }
    })
    const data = await responseUser.json()
    const responseImage = await fetch(`http://localhost:8000/Usuarios/atualiza-foto/${matricula}`, {
      method: "POST",
      body: formData,
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
    data = await responseImage.json()
  }

  return (
    <div>
      <form onSubmit={submitForm}>
        <div>
          <label htmlFor="matricula">
            Matrícula
          </label>
          <input
            type="text"
            id="matricula"
            name="matricula"
            autoComplete="matricula"
            required
            value={matricula}
            onChange={(e) => setMatricula(e.target.value)}
        />
        </div>
        <div>
          <label htmlFor="email">
            Email
          </label>
          <input
            type="text"
            id="email"
            name="email"
            autoComplete="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
        />
        </div>
        <div>
          <label htmlFor="password">
            Senha
          </label>
          <input
            type="password"
            id="password"
            name="password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
        />
        </div>
        <div>
          <label htmlFor="passwordConfirm">
            Confirme a Senha
          </label>
          <input
            type="password"
            id="passwordConfirm"
            name="passwordConfirm"
            required
            value={passwordConfirm}
            onChange={(e) => setPasswordConfirm(e.target.value)}
        />
        </div>
        <div>
          <label htmlFor="curso">
            Curso
          </label>
          <input
            type="text"
            id="curso"
            name="curso"
            autoComplete="curso"
            required
            value={curso}
            onChange={(e) => setCurso(e.target.value)}
        />
        </div>
        <div>
          <label htmlFor="imagem">
            Imagem de perfil
          </label>
          <input
            type="file"
            id="imagem"
            name="imagem"
            autoComplete="imagem"
            required
            onChange={(e) => setImagem(e.target.files[0])}
        />
        </div>
        <div>
          <label htmlFor="nome">
            Nome Completo
          </label>
          <input
            type="text"
            id="nome"
            name="nome"
            autoComplete="nome"
            required
            value={nome}
            onChange={(e) => setNome(e.target.value)}
        />
        </div>
        <div>
          <input
            type="submit"
            value="Cadastre-se"
          />
        </div>
      </form>
    </div>
  );
}