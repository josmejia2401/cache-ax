const net = require('net');
import { CommonUtil } from "./utils";

export class CacheAxClient {
    private client: any;
    private isUsed: boolean;
    private port: number;
    private host: string | undefined;
    private options: any | undefined;
    constructor(port = 63456, host = undefined, options?: { timeAlive: number }) {
        this.client = null;
        this.isUsed = false;
        this.port = port;
        this.host = host;
        this.options = options;
    }

    private async open() {
        this.isUsed = true;
        return new Promise((resolve) => {
            this.client = net.connect({ port: this.port, host: this.host }, () => {
                this.connected();
                resolve(true);
            });
        });
    }

    private connected() {
        this.client.on('error', (error: any) => console.log("error", error));
        this.client.on('lookup', (err: any, address: any, family: any, host: any) => console.log("lookup", err, address, family, host));
        this.client.on('timeout', () => this.client.end());
        this.client.setTimeout(5000);
    }

    private async sendMessage(message: any, fn: any) {
        if (this.isUsed) throw new Error("Not cant used");
        await this.open();
        this.client.on('data', (data: any) => {
            try {
                const dataAsString = data.toString();
                const response = CommonUtil.parse(dataAsString);
                fn(response);
            } catch (error) {
                throw error;
            } finally {
                this.client.end();
            }
        });
        this.client.write(JSON.stringify(message));
        return;
    }

    async get(key: string, name = "") {
        return new Promise((resolve, reject) => {
            try {
                const request = {
                    "operation": "GET",
                    "data": {
                        "tableName": name,
                        "key": key,
                    }
                };
                this.sendMessage(request, (response: any) => resolve(response));
            } catch (error) {
                reject(error);
            }
        });
    }

    async getAll(name = "") {
        return new Promise((resolve, reject) => {
            try {
                const request = {
                    "operation": "GET_ALL",
                    "data": {
                        "tableName": name,
                    }
                };
                this.sendMessage(request, (response: any) => resolve(response));
            } catch (error) {
                reject(error);
            }
        });
    }

    async set(key: string, value: any, name = "") {
        return new Promise((resolve, reject) => {
            try {
                const request = {
                    "operation": "SET",
                    "data": {
                        "tableName": name,
                        "key": key,
                        "value": value,
                        "timeAlive": this.options?.timeAlive
                    }
                };
                this.sendMessage(request, (response: any) => resolve(response));
            } catch (error) {
                reject(error);
            }
        });
    }

    async clean(name = "") {
        return new Promise((resolve, reject) => {
            try {
                const request = {
                    "operation": "CLEAN",
                    "data": {
                        "tableName": name,
                    }
                };
                this.sendMessage(request, (response: any) => resolve(response));
            } catch (error) {
                reject(error);
            }
        });
    }

    async remove(key: string, name = "") {
        return new Promise((resolve, reject) => {
            try {
                const request = {
                    "operation": "REMOVE",
                    "data": {
                        "tableName": name,
                        "key": key
                    }
                };
                this.sendMessage(request, (response: any) => resolve(response));
            } catch (error) {
                reject(error);
            }
        });
    }

    async size(name = "") {
        return new Promise((resolve, reject) => {
            try {
                const request = {
                    "operation": "SIZE",
                    "data": {
                        "tableName": name,
                    }
                };
                this.sendMessage(request, (response: any) => resolve(response));
            } catch (error) {
                reject(error);
            }
        });
    }
}
