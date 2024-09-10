import * as bcrypt  from 'bcryptjs';
import { QueryInterface } from 'sequelize';

const SALT_ROUNDS = process.env.BCRYPT_SALT_ROUNDS || 10;

export default {
  up: async (queryInterface: QueryInterface) => {
    await queryInterface.bulkInsert('users', [
      {
        username: 'Admin',
        email: 'admin@admin.com',
        password: bcrypt.hashSync('secret_admin', SALT_ROUNDS)
      },
    ], {});
  },

  down: async (queryInterface: QueryInterface) => {
    await queryInterface.bulkDelete('users', {});
  },
}
