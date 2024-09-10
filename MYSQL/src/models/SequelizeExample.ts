import {
  DataTypes,
  Model,
  InferAttributes,
  InferCreationAttributes,
} from 'sequelize';
import db from '.';

class SequelizeExample extends Model<InferAttributes<SequelizeExample>,
InferCreationAttributes<SequelizeExample>> {
  declare id: number;

  declare username: string;

  declare email: string;

  declare password: string;
}

SequelizeExample.init({
  id: {
    type: DataTypes.INTEGER,
    allowNull: false,
    primaryKey: true,
    autoIncrement: true,
  },
  username: {
    type: DataTypes.STRING(50),
    allowNull: false,
  },
  email: {
    type: DataTypes.STRING(50),
    allowNull: false,
  },
  password: {
    type: DataTypes.STRING(50),
  },
}, {
  sequelize: db,
  modelName: 'examples',
  timestamps: false,
  underscored: true,
});

export default SequelizeExample;
