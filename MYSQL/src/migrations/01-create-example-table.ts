import { Model, QueryInterface, DataTypes } from 'sequelize';
import { IExample } from '../Interface/IExample';

export default {
  up(queryInterface: QueryInterface) {
    return queryInterface.createTable<Model<IExample>>('Example', {
        id: {
            type: DataTypes.INTEGER,
            allowNull: false,
            primaryKey: true,
            autoIncrement: true,
          },
          username: {
            type: DataTypes.STRING,
            allowNull: false,
          },
          email: {
            type: DataTypes.STRING,
            allowNull: false,
          },
          password: {
            type: DataTypes.STRING,
          },
    });
  },
  down(queryInterface: QueryInterface) {
    return queryInterface.dropTable('Example');
  },
};