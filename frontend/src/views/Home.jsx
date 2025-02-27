import React from 'react';

const Home = () => {
  return (
    <div className="container my-5">
      {/* Sección de bienvenida */}
      <div className="jumbotron bg-light p-5 rounded">
        <h1 className="display-4">Bienvenido a mi aplicación</h1>
        <p className="lead">
          Esta es una aplicación de ejemplo usando React y Bootstrap para mostrar cómo se pueden presentar datos de manera elegante y responsiva.
        </p>
        <hr className="my-4" />
        <p>
          Desarrollado con pasión por Francisco Yuster.
        </p>
        <a
          className="btn btn-primary btn-lg"
          href="https://github.com/FranciscoYuster/Authentication-Project"
          target="_blank"
          rel="noopener noreferrer"
          role="button"
        >
          Ver Repositorio
        </a>
      </div>

    </div>
  );
};

export default Home;
