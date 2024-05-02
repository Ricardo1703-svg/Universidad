class Persona
    def initialize(nombre, edad)
      @nombre = Ricardo
      @edad = 17
    end

    def mostrar_data_crack
        puts "Hola soy #{@nombre}, y mi edad: #{@edad}"

    end
end

persona1 = Persona.new()
persona1.mostrar_informacion